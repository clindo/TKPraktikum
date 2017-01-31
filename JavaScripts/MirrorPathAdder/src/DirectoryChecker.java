import static java.nio.file.StandardWatchEventKinds.ENTRY_CREATE;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Enumeration;
import java.util.Properties;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

/**
 *
 * @author Clindo
 */

/***
 * 
 * This DirectoryChecker uses the Watch Service API for checking the addition of
 * files in specified path This is developed as a part of TK Praktikum at TU
 * Darmstadt, Germany.
 *
 */
public class DirectoryChecker {

	public static Logger logger = Logger.getLogger("MyLog");  
    public static FileHandler fh; 

    
    public static DateFormat df = new SimpleDateFormat("dd/MM/yy HH:mm:ss");
    public static Date dateobj = new Date();
    
	public static void main(String[] args) {
	    logger.setUseParentHandlers(false);
		/*
		 * Logger logger = Logger.getLogger(DirectoryChecker.class);
		 * 
		 * Appender Notconsole = new ConsoleAppender(); Logger root =
		 * Logger.getRootLogger(); root.addAppender(Notconsole);
		 * 
		 * BasicConfigurator.configure();
		 * logger.info("This is my first log4j's statement");
		 */
		String DirPath;
		try {

			fh = new FileHandler("LogFile.log");
			logger.addHandler(fh);
	        SimpleFormatter formatter = new SimpleFormatter();  
	        fh.setFormatter(formatter);  
	       
			
	        logger.info("---THE LOG FOR DIRECTORY CHECKER STARTS HERE--- "+df.format(dateobj));  
			File file = new File("config.xml");
			FileInputStream fileInput = new FileInputStream(file);
			Properties properties = new Properties();
			properties.loadFromXML(fileInput);
			fileInput.close();

			Enumeration enuKeys = properties.keys();

			String propName = (String) enuKeys.nextElement();
			String value = properties.getProperty(propName);
			// System.out.println(propName + ": " + value);

			 DirPath = value;
			/*
			 * while (enuKeys.hasMoreElements()) { String key = (String)
			 * enuKeys.nextElement(); String value =
			 * properties.getProperty(key); System.out.println(key + ": " +
			 * value); }
			 */

			WatchService watcher = FileSystems.getDefault().newWatchService();
			Path dir = Paths.get(DirPath);
			dir.register(watcher, ENTRY_CREATE); // , ENTRY_DELETE, ENTRY_MODIFY

			logger.info("Watch Service registered for dir: "
					+ dir.getFileName()+df.format(dateobj));
			
			while (true) {
				WatchKey key;
				try {
					key = watcher.take();
				} catch (InterruptedException ex) {
					return;
				}

				for (WatchEvent<?> event : key.pollEvents()) {
					WatchEvent.Kind<?> kind = event.kind();

					@SuppressWarnings("unchecked")
					WatchEvent<Path> ev = (WatchEvent<Path>) event;
					Path fileName = ev.context();

					// System.out.println(kind.name() + ": " + fileName);

					/*
					 * if (kind == ENTRY_MODIFY && fileName.toString().equals(
					 * "DirectoryChecker.java"))
					 */

					if (kind == ENTRY_CREATE) {

						logger.info("---New Folder is created by Camtasia--- "+df.format(dateobj)); 
						
						String htmlName=fileName.toString()+".html";
						
						System.out.println(htmlName);
						String htmlPath=DirPath+"/"+htmlName;
						appendXml(htmlPath);

					}
				}

				boolean valid = key.reset();
				if (!valid) {
					break;
				}
			}

		} catch (IOException ex) {
			System.err.println(ex);
		}
	}
	

	
	
	public static void appendXml(String htmlPath) {

		System.out.println("Append xml here");

		BufferedWriter bw = null;

		try {
			// APPEND MODE SET HERE
			bw = new BufferedWriter(new FileWriter(
					"D:/Master Studies/WS16-17/TKPraktikum/root.conf", true));
			String toAppend= "Alias /TK/WeekNumber ";
			
			logger.info("---Alias is appended to Apache Root--- "+df.format(dateobj)); 
			
			bw.write(toAppend+htmlPath);
			bw.newLine();
			bw.flush();
		} catch (IOException ioe) {
			ioe.printStackTrace();
		} finally { // always close the file
			if (bw != null)
				try {
					bw.close();
				} catch (IOException ioe2) {
					// just ignore it
				}
		} // end try/catch/finally

	} // end test()

}