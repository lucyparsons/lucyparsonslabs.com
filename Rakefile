require 'date'

task :dev do
  sh "while true ; do bundle exec jekyll serve --config _config.yml,_config_dev.yml ; sleep 10 ; done"
end

task :updatecanary do
  # this doesn't work yet
  "We have not been contacted by any government agencies requesting information about our workshop attendees or website visitors. This post will be updated monthly. Last updated #{Date.today.strftime("%B %e, %Y")}."
end
