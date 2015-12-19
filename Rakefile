require 'date'

desc "Run a dev server at localhost:4000"
task :dev do
  sh "while true ; do bundle exec jekyll serve --config _config.yml,_config_dev.yml ; sleep 10 ; done"
end


desc "Update the warrant canary with your gpg key"
task :updatecanary do
 canarytext = "We have not been contacted by any government agencies requesting information about our workshop attendees or website visitors. This post will be updated monthly. Last updated #{Date.today.strftime("%B %e, %Y")}."
 sh "echo #{canarytext} | gpg --clearsign > _includes/canary.txt"
end
