Vim�UnDo� ��/�yt�~�h�l"`l.�mʾ�e׃:�7�S     g    s3cmd sync --follow-symlinks --acl-public /home/arch/local-repo/ s3://rhinocerose-arch/repo/x86_64/   �                          _��C    _�                        /    ����                                                                                                                                                                                                                                                                                                                                                             _x�r     �              E     arduino-cli compile --fqbn arduino:avr:uno:cpu=atmega328 "$argv"5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             _x�t     �              D     arduino-cli compile --fqbn arduino:avr:unocpu=atmega328 "$argv"5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             _x�u     �              A     arduino-cli compile --fqbn arduino:avr:uno=atmega328 "$argv"5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             _x�u     �              @     arduino-cli compile --fqbn arduino:avr:unoatmega328 "$argv"5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             _x�w    �              6     arduino-cli compile --fqbn arduino:avr:uno"$argv"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _y�+     �              N    sudo avrdude -c avrisp2 -p m328p -U flash:w:build/arduino.avr.nano/"$argv"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _y�.    �              J     avrdude -c avrisp2 -p m328p -U flash:w:build/arduino.avr.nano/"$argv"5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             _y�`    �                  �            5�_�      
           	      J    ����                                                                                                                                                                                                                                                                                                                                                             _y�     �              J    arduino-cli upload -P avrispmkii --fqbn arduino:avr:nano:cpu=atmega3285�_�   	              
      K    ����                                                                                                                                                                                                                                                                                                                                                             _y�    �              S    arduino-cli upload -P avrispmkii --fqbn arduino:avr:nano:cpu=atmega328  "$argv"5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             _y��     �              7     arduino-cli compile --fqbn arduino:avr:uno "$argv"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _y��    �              N     sudo avrdude -c avrisp2 -p m328p -U flash:w:build/arduino.avr.uno/"$argv"5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _z>]    �   �   �        	sudo pacman -Syyu5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             _{F�     �   �   �            �   �   �      5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _{F�     �   �   �            �   �   �      5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _{F�    �   �   �            �   �   �      5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             _{Gq     �   �   �         5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _{G�     �   �   �        l    sudo reflector --latest 200 --protocol http --protocol https --sort rate --save /etc/pacman.d/mirrorlist5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _{G�     �   �   �        k    sudo reflector --latest 20 --protocol http --protocol https --sort rate --save /etc/pacman.d/mirrorlist    �   �   �            �   �   �      5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _{G�     �   �   �        k    sudo reflector --latest 20 --protocol http --protocol https --sort rate --save /etc/pacman.d/mirrorlist5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _{G�   
 �   �   �        g     reflector --latest 20 --protocol http --protocol https --sort rate --save /etc/pacman.d/mirrorlist5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             _��K     �   �   �         �   �   �      5�_�                    �   >    ����                                                                                                                                                                                                                                                                                                                                                             _��h     �   �   �            �   �   �      5�_�                    �   .    ����                                                                                                                                                                                                                                                                                                                                                             _���    �   �   �        \    s3cmd sync --follow-symlinks --acl-public local-repo/ s3://rhinocerose-arch/repo/x86_64/5�_�                    �   	    ����                                                                                                                                                                                                                                                                                                                                                             _���    �   �   �            �   �   �      5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _���    �   �   �          g    s3cmd sync --follow-symlinks --acl-public /home/arch/local-repo/ s3://rhinocerose-arch/repo/x86_64/5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _���    �   �   �          i    # s3cmd sync --follow-symlinks --acl-public /home/arch/local-repo/ s3://rhinocerose-arch/repo/x86_64/5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             _��@     �   �   �          @    aur sync -d rhinocerose --root /home/arch/local-repo "$argv"5�_�                     �       ����                                                                                                                                                                                                                                                                                                                                                             _��B    �   �   �        g    s3cmd sync --follow-symlinks --acl-public /home/arch/local-repo/ s3://rhinocerose-arch/repo/x86_64/5��