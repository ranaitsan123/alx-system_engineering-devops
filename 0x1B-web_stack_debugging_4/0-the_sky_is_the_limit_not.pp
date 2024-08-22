# This Puppet manifest configures Nginx to handle high traffic more effectively

exec { 'fix--for-nginx':
  command => 'service nginx reload',
  path    => ['/usr/bin', '/bin'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['fix--for-nginx'],
}
