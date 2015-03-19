<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:y="http://www.suse.com/1.0/yast2ns">
 <xsl:output method="xml" encoding="UTF-8"/>
 <xsl:template match="@*|node()">
  <xsl:copy>
   <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
 </xsl:template>
 <xsl:template match="/y:productDefines/y:software/y:extra_urls/y:extra_url[y:baseurl][contains(y:baseurl, 'non-oss')]"/>
</xsl:stylesheet>
