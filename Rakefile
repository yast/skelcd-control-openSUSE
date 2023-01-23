require "yast/rake"

Yast::Tasks.configuration do |conf|
  conf.obs_api = "https://api.opensuse.org"
  conf.obs_target = "openSUSE_Leap_15.5"
  conf.obs_sr_project = "openSUSE:Leap:15.5"
  conf.obs_project = "YaST:openSUSE:15.5"
  #lets ignore license check for now
  conf.skip_license_check << /.*/
  conf.exclude_files << /README.md/ #do not pack readme
end

desc "Generate *-promo package files"
task :create_promo do
  Dir.chdir("package") do
    sh "./pre_checkin.sh"
  end
end

# generate the *-promo files when creating the tarball
task :tarball => :create_promo
