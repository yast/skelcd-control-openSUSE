require "yast/rake"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end


# hacks to avoid using the version number in the tarball name,
# the version is automatically generated from the *.changes
# by get_version_number.sh script in OBS


# clear version:bump - as mentined above the version is updated in OBS,
# "version:bump" task does not make sense here
Rake::Task["version:bump"].clear_actions


# TODO: add support to the packaging tasks to exclude version in the tarball name

def package_file_name
  config = Packaging::Configuration.instance
  # package file name _without_ version
  config.package_name
end

# create new package task
def create_package_task
  require 'rake/packagetask'
  config = Packaging::Configuration.instance
  # use the :noversion option instead of the default
  Rake::PackageTask.new(config.package_name, :noversion) do |p|
    p.need_tar_bz2 = true
    p.package_dir = Packaging::Configuration.instance.package_dir

    add_git_files p

    config.include_files.each { |f| p.package_files.include f }
    #ignore itself
    p.package_files.exclude "./#{p.package_dir}"

    config.exclude_files.each { |f| p.package_files.exclude f }
  end
end

