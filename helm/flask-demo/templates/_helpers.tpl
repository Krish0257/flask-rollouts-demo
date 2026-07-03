{{/*
Expand the chart name.
*/}}
{{- define "flask-demo.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Create a fully qualified application name.
*/}}
{{- define "flask-demo.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name (include "flask-demo.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end }}

{{/*
Chart name and version.
*/}}
{{- define "flask-demo.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Common labels shared by all resources.
*/}}
{{- define "flask-demo.labels" -}}
helm.sh/chart: {{ include "flask-demo.chart" . }}
app.kubernetes.io/name: {{ include "flask-demo.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/component: application
app.kubernetes.io/part-of: flask-demo
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels.
These labels must remain immutable.
*/}}
{{- define "flask-demo.selectorLabels" -}}
app.kubernetes.io/name: {{ include "flask-demo.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Service Account name.
*/}}
{{- define "flask-demo.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
{{- default (include "flask-demo.fullname" .) .Values.serviceAccount.name -}}
{{- else -}}
{{- default "default" .Values.serviceAccount.name -}}
{{- end -}}
{{- end }}