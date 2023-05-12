require "yast/rake"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
  conf.exclude_files << /README.md/ #do not pack readme
end

# this package uses the date versioning in master (for openSUSE Tumbleweed),
# replace the standard yast task implementation
Rake::Task[:'version:bump'].clear
namespace :version do
  desc "Update version in the package/skelcd-control-openSUSE.spec file"
  task :bump do
    spec_file = "package/skelcd-control-openSUSE.spec"
    spec = File.read(spec_file)

    # parse the current version, it can be in <date> or <date>.<release> format
    _, version, release = spec.match(/^\s*Version:\s*(\w+)(?:\.(\w+))?$/).to_a
    # use the UTC time to avoid conflicts when updating from different time zones
    date = Time.now.utc.strftime("%Y%m%d")

    # add a release version if the package has been already updated today
    new_version = if version == date
      # if the release was missing it starts from 1
      "#{date}.#{release.to_i + 1}"
    else
      "#{date}"
    end

    puts "Updating to #{new_version}"
    spec.gsub!(/^\s*Version:.*$/, "Version:        #{new_version}")
    File.write(spec_file, spec)
  end
end
