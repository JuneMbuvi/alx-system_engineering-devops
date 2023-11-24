#installs falsk from pip3 using Puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  name     => 'flask',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  name     => 'Werkzeug',
}
