# 100-puppet_ssh_config.pp

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
  notify => Exec['reload_ssh'],
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
  notify => Exec['reload_ssh'],
}

exec { 'reload_ssh':
  command     => '/etc/init.d/ssh reload',
  refreshonly => true,
}

