variable "k8s_version" {
  default = "1.25"
}

variable "enable_private" {
  default = false
}

variable "public_az" {
  type        = string
  description = "Public availability zone"
  default     = "a"
}

variable "private_az" {
  type        = string
  description = "Private availability zone"
  default     = "b"
}
