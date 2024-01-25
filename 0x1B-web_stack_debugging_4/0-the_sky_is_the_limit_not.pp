# 0-the_sky_is_the_limit_not.pp

file { '/etc/security/limits.conf':
  content => "*
               soft    nofile     8192
               *       hard    nofile     8192
               root    hard    core      100000
               *       hard    rss       10000
               @student hard    nproc     20
               @faculty soft    nproc     20
               @faculty hard    nproc     50
               ftp     hard    nproc     0
               ftp     -       chroot    /ftp
               @student -       maxlogins 4
  ",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/security/limits.conf'],
}
