# Using puppet to fix type in .php file.
exec { 'sed':
  path    => '/bin/',
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php"
}
