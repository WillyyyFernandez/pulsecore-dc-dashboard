variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "Application name"
  type        = string
  default     = "dc-dashboard"
}

variable "container_port" {
  description = "Port the container listens on"
  type        = number
  default     = 8501
}
