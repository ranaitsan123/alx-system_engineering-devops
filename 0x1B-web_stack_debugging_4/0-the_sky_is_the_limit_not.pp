# Increase the ULIMIT of the default file
file { '/etc/default/nginx':
  ensure  => file,
  content => "ulimit -n 4096",
}

# Restart Nginx
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/default/nginx'],
}
