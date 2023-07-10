# file: 101-setup_web_static.pp - setup server prepping for static deploy:

package { 'nginx':
  ensure => 'installed',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Hello World!\n  </body>\n</html>\n',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/etc/nginx/sites-available/default':
  content => "server {
    listen      80 default_server;
    listen      [::]:80 default_server;
    root        /var/www/html;
    index       index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location     /redirect_me {
        return  301 https://stackoverflow.com/;
    }

    error_page   404 /404.html;
    location     /404 {
        root   /var/www/html;
        internal;
    }

    add_header X-Served-By ${hostname};
}\n",
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
