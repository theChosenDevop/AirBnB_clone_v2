# redo of task 0 using puppet
# Install Nginx if it not already installed
class { 'nginx': }

# Create the necessary directories
file { '/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Hello, World!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        location /hbnb_static/ {
            alias /data/web_static/current/;
        }
    }
  ",
}

# Restart Nginx
service { 'nginx':
  ensure => 'running',
  enable => true,
}
