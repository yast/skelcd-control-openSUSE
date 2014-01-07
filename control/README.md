Products:
---------

For the various products starting from SuSE Linux 9.1, several product
control packages have been created and more will follow for future
products. Those special package are used when creating the CDs and they
install the control file into the first CD of the product (to the
root directory with name `/control.xml`).


Add-On Products:
----------------

File `add-on-template_installation.xml` is a template for adding a workflow to the
Language Add-On Product. It should be saved under the root directory
of the add-on product as `installation.xml`.

Currently it uses these clients:
  - inst_language_add-on


Control file validation:
------------------------

Run command

    xmllint --noout --relaxng /usr/share/YaST2/control/control.rng *.xml

or simply

    make check

