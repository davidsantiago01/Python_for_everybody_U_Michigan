<xs:element name ="person">
  <xs:complexType>
    <xs:sequence>
      <xs:element name ="full_name" type="xs.string"
      minOccurs="1" maxOccurs="1"/>
    <xs:element name="child_name"type="xs.string"
    minOccurs="0" maxOccurs="10"/>
   <xs:sequence> 
  <xs:complexType>
<xs:element name ="person">

<person>
<full_name>Tove Refsness</full_name>
<child_name>Hege</child_name>
<child_name>Stale</child_name>
<child_name>Jim</child_name>
<child_name>Borge</child_name>
<person>


