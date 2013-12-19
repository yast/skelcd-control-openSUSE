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
</xsl:stylesheet>
