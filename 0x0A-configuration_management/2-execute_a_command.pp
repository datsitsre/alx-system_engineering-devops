# Create a manifest that kills a process named Killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}

