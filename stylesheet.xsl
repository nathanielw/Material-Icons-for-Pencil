<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.evolus.vn/Namespace/Pencil"         xmlns:p="http://www.evolus.vn/Namespace/Pencil"
        xmlns:svg="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0">
    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="files">
        <Shapes
        id="nz.nwatson.MaterialIcons"
        displayName="Material Icons"
        description="Material Design Icons. Icons from https://materialdesignicons.com/
        &#13;
        &#13;This Pencil stencil collection consists of icons from:
        &#13; - 'Material Design Icons' by Google (http://google.github.io), used under an Attribution 4.0 International license (http://creativecommons.org/licenses/by/4.0/).
        &#13; - MaterialDesignIcons.com contributors, used under the SIL Open Font License 1.1 (https://github.com/Templarian/MaterialDesign/blob/master/license.txt)
        &#13;
        &#13;Please check the linked licenses for each icon's conditions of use.
        &#13;
        &#13;Source code for generating this stencil collection can be found at https://github.com/nathanielw/Material-Icons-for-Pencil and is licensed under the MIT License."
        author="Icons by Google (google.github.io) and MaterialDesignIcons.com contributors. Pencil Stencil by Nathaniel Watson (nwatson.nz)"
        url="https://github.com/nathanielw/Material-Icons-for-Pencil">

            <Properties>
                <PropertyGroup>
                    <Property name="fillColor" displayName="Icon color" type="Color">#000000ff</Property>
                </PropertyGroup>
            </Properties>

            <xsl:apply-templates/>
        </Shapes>
    </xsl:template>

    <xsl:template match="files/file">
        <xsl:variable name="svg" xmlns:svg="http://www.w3.org/2000/svg" select="document(.)/svg:svg" />

        <Shape id="{./@id}" displayName="{./@name}" icon="{./@icon}">
            <Properties>
                <PropertyGroup>
                    <Property name="box" type="Dimension" p:lockRatio="true"><xsl:value-of select="$svg/@width" />,<xsl:value-of select="$svg/@height" /></Property>
                </PropertyGroup>
                <PropertyGroup name="Background">
                    <Property name="fillColor" displayName="Color" type="Color"><E>$$fillColor</E></Property>
                </PropertyGroup>
            </Properties>

            <Behaviors>
                <For ref="icon">
                    <Transform>scale($box.w/<xsl:value-of select="$svg/@width" />, $box.h/<xsl:value-of select="$svg/@height" />)</Transform>
                    <Fill>$fillColor</Fill>
                </For>
            </Behaviors>
            <p:Content xmlns:p="http://www.evolus.vn/Namespace/Pencil" xmlns="http://www.w3.org/2000/svg">
                <g id="icon">
                    <xsl:copy-of select="$svg/*"/>
                </g>
            </p:Content>
        </Shape>
    </xsl:template>
</xsl:stylesheet>
