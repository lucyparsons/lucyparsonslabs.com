require 'date'

CONFIG = { 
  'prod' => {
    'additional_configs' => nil,
    's3_bucket' => 'lucyparsonslabs-prod',
    'distribution_id' => 'E26W44TW4Z3F86',
    'cache_control_timeout' => '600',
    'webserver' => 'lucyparsonslabs.com',
  },
  'staging' => {
    'additional_configs' => '_config_staging.yml',
    's3_bucket' => 'lucyparsonslabs-staging',
    'distribution_id' => 'E2WZU7A1UNKB2I',
    'cache_control_timeout' => '5',
  }
}

desc "Run a dev server at localhost:4000"
task :dev do
  sh "bundle exec jekyll serve --config _config.yml,_config_dev.yml"
end

desc 'Invalidate the staging cloudfront distribution'
task :invalidate do
  invalidate_cloudfront_distro CONFIG['staging']['distribution_id']
end

desc 'Build the site'
task :build do
  sh 'bundle exec jekyll build'
end

desc 'Publish to staging via aws cli s3 upload'
task :deploy do
  puts 'Building the site for staging'
  publish_to_s3(CONFIG['staging'])
  puts 'New content copied to https://staging.lucyparsonslabs.com'
end

desc 'Publish to prod via aws cli s3 upload'
task :deploy_prod do
  puts 'Building the site for production'
  publish_to_s3(CONFIG['prod'])
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

  Dir.chdir(File.dirname(__FILE__)) do
    sh "echo \"#{canarytext}\" | gpg --clearsign > _includes/canary.txt"
  end
end

def publish_to_s3(site_config)
  additional_configs = site_config['additional_configs']
  s3_bucket = site_config['s3_bucket']
  cache_control_timeout = site_config['cache_control_timeout']
  cloudfront_distro_id = site_config['distribution_id']
  Dir.chdir(File.dirname(__FILE__)) do
    if additional_configs
      config = ['_config.yml', additional_configs].join(',')
    else
      config = '_config.yml'
    end
    sh "rm -r _site || true"
    sh "bundle exec jekyll build --config #{config}"
    puts "Publishing the contents of _site to s3 bucket #{s3_bucket}"
    sh "aws s3 sync _site s3://#{s3_bucket}/ --delete --cache-control max-age=#{cache_control_timeout}"
    invalidate_cloudfront_distro(cloudfront_distro_id)
  end
end

def invalidate_cloudfront_distro(distribution_id)
  sh "aws cloudfront create-invalidation --distribution-id #{distribution_id} --paths '/*'"
end
