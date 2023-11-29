# Installs flask

package { 'python3-pip':
  ensure => installed,
}

package { 'python3-flask':
  ensure   => installed,
  require  => Package['python3-pip'],
  provider => 'yum',
}
