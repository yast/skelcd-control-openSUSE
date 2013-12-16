<!--
  Definition of the control.openSUSE.xml -> control.openSUSE-promo.xml transformation.
  Replace the <products_supported_for_upgrade> node by definition from
  control.openSUSE-promo.changes.xml file
-->
<xsl:stylesheet version="1.0"
  xmlns:n="http://www.suse.com/1.0/yast2ns"
  xmlns:config="http://www.suse.com/1.0/configns"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="xml" indent="yes"/>

 <xsl:template match="node()|@*">
  <xsl:copy>
   <xsl:apply-templates select="node()|@*"/>
  </xsl:copy>
 </xsl:template>

 <xsl:template match="n:products_supported_for_upgrade">
    <xsl:copy-of select="document('control.openSUSE-promo.changes.xml')/*/*/n:products_supported_for_upgrade"/>
 </xsl:template>
</xsl:stylesheet>
