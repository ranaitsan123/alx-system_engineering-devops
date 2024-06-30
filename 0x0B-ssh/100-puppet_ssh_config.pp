# 100-puppet_ssh_config.pp

# Ensure SSH client configuration file exists
file { '/home/ubuntu/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

# Ensure SSH client configuration file has necessary settings
file_line { 'Turn off passwd auth':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'PasswordAuthentication no',
  ensure => present,
}

file_line { 'Declare identity file':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  ensure => present,
}
