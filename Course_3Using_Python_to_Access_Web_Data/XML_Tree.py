#Example of XML as a Tree

<a> #open tag
  <b> X </b> #children of a
  <c> #children of a
    <d> Y </d> #children of c
    <e> Z </e> #children of c
  </c> #close c
</a> #close tag

 
# XML and Attributes
 <a>
  <b W="5"> X </b> #5 attribute of W, X = text node
  <c>
    <d> Y </d>
    <e> Z </e>
  </c>
</a>


#XML as Paths
<a> #open tag
  <b> X </b> #children of a  
  <c> #children of a                  /a/b   X
    <d> Y </d> #children of c         /a/c/d Y
    <e> Z </e> #children of c         /a/c/e Z 
  </c> #close c
</a> #close tag


