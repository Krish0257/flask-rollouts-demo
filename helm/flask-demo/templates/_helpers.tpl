{{/*
Expand the chart name.
*/}}
{{- define "flask-demo.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Create a fully qualified app name.
*/}}
{{- define "flask-demo.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name (include "flask-demo.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

{{/*
Chart name and version.
*/}}
{{- define "flask-demo.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" }}
{{- end }}

{{/*
Common labels.
*/}}
{{- define "flask-demo.labels" -}}
helm.sh/chart: {{ include "flask-demo.chart" . }}
app.kubernetes.io/name: {{ include "flask-demo.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels.
*/}}
{{- define "flask-demo.selectorLabels" -}}
app.kubernetes.io/name: {{ include "flask-demo.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}