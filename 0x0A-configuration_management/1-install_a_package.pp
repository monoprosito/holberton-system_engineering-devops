# Install a package using Puppet

exec { 'install ruby':
  command => '/usr/bin/apt-get install -y ruby'
}

exec { 'install puppet-lint':
  command => '/usr/bin/gem install puppet-lint -v 2.1.1'
}

package { 'ruby':
  ensure => 'installed',
  before => Exec['install ruby']
}

package { 'puppet-lint':
  ensure  => 'installed',
  before  => Exec['install puppet-lint'],
  require => Package['ruby']
}
