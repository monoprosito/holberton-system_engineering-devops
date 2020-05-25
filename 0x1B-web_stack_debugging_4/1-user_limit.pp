# Set a new soft and hard value to the limit
# of max open files for all the system

exec { 'change-max-open-files-hard-limit':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/hard nofile [0-9]\+/hard nofile 4000/g'"
}

exec { 'change-max-open-files-soft-limit':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/soft nofile [0-9]\+/soft nofile 3000/g'"
}
