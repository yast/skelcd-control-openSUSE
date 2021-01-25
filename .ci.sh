#! /bin/bash

set -e -x

make -C control check

# the "yast-travis-ruby" script is included in the base yastdevel/ruby image
# see https://github.com/yast/docker-yast-ruby/blob/master/yast-travis-ruby
yast-travis-ruby

# explicitly check the changelog sequence, the source_validator is fine if at least one
# *.changes file is OK, but here we need to be sure that both are correct
/usr/lib/obs/service/source_validators/helpers/convert_changes_to_rpm_changelog --check < package/skelcd-control-openSUSE.changes
/usr/lib/obs/service/source_validators/helpers/convert_changes_to_rpm_changelog --check < package/skelcd-control-openSUSE-promo.changes

