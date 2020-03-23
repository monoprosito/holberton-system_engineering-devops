# Kills a process named 'killmenow' using Puppet

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
