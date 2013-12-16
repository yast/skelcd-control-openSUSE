<!--
  Definition of the control.SLES.xml -> control.SLES-for-VMware.xml transformation.
  Remove the system scenario definitions, they do not make sense in VMware.
-->

<xsl:stylesheet version="1.0"
  xmlns:n="http://www.suse.com/1.0/yast2ns"
  xmlns:config="http://www.suse.com/1.0/configns"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="xml" indent="yes"/>
<xsl:strip-space elements="n:default_system_scenario"/>

  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <!-- match the preceding comment, see http://stackoverflow.com/questions/2613159/xslt-and-xpath-match-preceding-comments -->
  <xsl:template match="comment()[following-sibling::*[1]/self::n:system_scenarios]">
    <xsl:comment> There are no system scenarios, VMware is always virtual with a defined set of packages </xsl:comment>
  </xsl:template>
  <xsl:template match="n:system_scenarios"/>

  <xsl:template match="comment()[following-sibling::*[1]/self::n:default_system_scenario]"/>
  <xsl:template match="n:default_system_scenario"/>

</xsl:stylesheet>
