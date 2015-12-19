require 'date'

desc "Run a dev server at localhost:4000"
task :dev do
  sh "bundle exec jekyll serve --config _config.yml,_config_dev.yml"
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
