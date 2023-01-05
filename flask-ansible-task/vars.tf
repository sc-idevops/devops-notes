variable "appName" {
  type = string
    default = "scard"
}

variable "port" {
  type = number
    default = 80
}

variable "subnets" {
  type = list
    default = ["subnet-0357bbe188bd1e4c8", "subnet-04ee363ec3c8a8fef", "subnet-075293e11cc798803"]
}

variable "hcstatuscode" {
  type = string
    default = "200"
}

variable "hostedZone" {
  type = string
    default = "Z370FY5A2PDAE"
}