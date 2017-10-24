require 'date'

desc "Run a dev server at localhost:4000"
task :dev do
  sh "bundle exec jekyll serve --config _config.yml,_config_dev.yml"
end


desc 'Build the site'
task :build do
  sh 'bundle exec jekyll build'
end

desc 'Publish to staging via rsync'
task :deploy do
  puts 'Building the site for staging'
  publish_to_s3('_config_staging.yml', 'lucyparsonslabs-staging', 5)
  puts 'New content copied to https://staging.lucyparsonslabs.com'
end

desc 'Publish to prod via rsync'
task :deploy_prod do
  puts 'Building the site for production'
  publish_to_s3(nil, 'lucyparsonslabs-prod', 600)
  publish_to_server(nil, 'lucyparsonslabs.com')
  puts 'New content copied to https://lucyparsonslabs.com'
end


desc "Update the warrant canary with your gpg key"
task :updatecanary do
# note: if you include any shell-special characters here, you get to fix the sh command
 canarytext = <<-END
We have not been contacted by any government agencies requesting\n
information about our workshop attendees or website visitors.\n
This post will be updated monthly.\n
Last updated #{Date.today.strftime("%B %e, %Y")}.
END
 sh "echo \"#{canarytext}\" | gpg --clearsign > _includes/canary.txt"
end

def publish_to_server(additional_configs, server)
  Dir.chdir(File.dirname(__FILE__))
  if additional_configs
    config = ['_config.yml', additional_configs].join(',')
  else
    config = '_config.yml'
  end
  sh "bundle exec jekyll build --config #{config}"
  puts 'Publishing the contents of _site'
  user = 'lpldeploy'
  path = '/var/www/lucyparsonslabs.com'
  sh "rsync -rtzh --delete _site/ #{user}@#{server}:#{path}"
end

def publish_to_s3(additional_configs, s3_bucket, cache_control_timeout)
  Dir.chdir(File.dirname(__FILE__))
  if additional_configs
    config = ['_config.yml', additional_configs].join(',')
  else
    config = '_config.yml'
  end
  sh "bundle exec jekyll build --config #{config}"
  puts "Publishing the contents of _site to s3 bucket #{s3_bucket}"
  sh "aws s3 sync _site s3://#{s3_bucket}/ --delete --cache-control max-age=#{cache_control_timeout}"
end

