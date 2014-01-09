require "yast/rake"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end

desc "Generate *-promo package files"
task :create_promo do
  Dir.chdir("package") do
    sh "./pre_checkin.sh"
  end
end

# generate the *-promo files when creating the tarball
task :tarball => :create_promo

