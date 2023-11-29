# Installs flask

class flask_install {
  package { 'python3-pip':
    ensure => installed,
  }

  package { 'Flask':
    ensure   => '2.
