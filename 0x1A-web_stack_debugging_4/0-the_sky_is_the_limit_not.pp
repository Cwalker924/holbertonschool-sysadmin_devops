# Change max file from 15 to 15000 then restart nginx
exec { 'change limit from 15 to 15000':
  path    => ['/usr/bin/','/usr/sbin/','/bin'],
  command => 'sed -i "s@ULIMIT=\"-n 15\"@ULIMIT=\"-n 15000\"@" /etc/default/nginx && service nginx restart',
}