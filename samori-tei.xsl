<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<!-- The template element with the match attribute -->
<xml:template match="/">
  <html>
    <body>
      <
      <h1>The History of Imam Samori</h1>
      <h1><xsl:value-of select="TEI/teiHeader/fileDesc/titleStmt/title"/></h1>
      <h2><xsl:value-of select="TEI/teiHeader/fileDesc/titleStmt/author"/></h2>
    </body>
  </html>
</xml:template>

</xsl:stylesheet>
