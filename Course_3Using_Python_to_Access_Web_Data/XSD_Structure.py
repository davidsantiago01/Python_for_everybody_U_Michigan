#XSD Structure

xs:element naranja
xs:sequence verde
xs:complexType amarillo

 <person> amarillo
  <lastname> Severance </lastname> naranja
  <age> 17 </age> naranja
  <dateborn>2001-04-17</dateborn> naranja
 <person> amarillo

 <xs:complexType name="person">
   <xs:sequence>
      <xs:element name="lastname" type="xs:string"/>
      <xs:element name="age" type="xs:integer"/>
      <xs:element name="dateborn" type="xs:date"/>
