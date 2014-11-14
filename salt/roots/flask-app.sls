include:
  - requirements

/home/vagrant/flask-venv:
  virtualenv.managed:
    - system_site_packages: False
    - requirements: /vagrant/requirements.txt

#pip:
  #- requirements: /vagrant/Backend/requirements.txt
  #- timeout: 20