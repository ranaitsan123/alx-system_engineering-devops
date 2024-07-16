# This Puppet manifest installs Flask version 2.1.0 and Werkzeug version 2.0.3 using pip3

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install the required versions of Flask and Werkzeug
exec { 'install_flask_and_werkzeug':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.0.3',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep 2.1.0 && /usr/bin/pip3 show Werkzeug | grep 2.0.3',
  require => Package['python3-pip'],
}
