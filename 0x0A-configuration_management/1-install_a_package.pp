# Install flask using pip3 platform puppet

package {'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
