# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  onlyif  => 'grep -q "ulimit -n 4096" /etc/default/nginx', # Ensure the change is applied only if not already set
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['fix--for-nginx'],
}
