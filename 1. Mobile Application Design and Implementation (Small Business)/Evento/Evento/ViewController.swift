//
//  ViewController.swift
//  Evento
//
//  Created by Anup Ahuje on 13/08/18.
//  Copyright © 2018 Events. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var tapOnMapViewRef: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        /* When user Tap on Map They will be redirected to iPhone Map */
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(imageTapped(tapGestureRecognizer:)))
        tapOnMapViewRef.isUserInteractionEnabled = true
        tapOnMapViewRef.addGestureRecognizer(tapGestureRecognizer)
        
    }
    
    /* This Method will be called when user tap on MAP Inage */
    @objc func imageTapped(tapGestureRecognizer: UITapGestureRecognizer)
    {
        let locationLat = "19.091183"
        let locationlong = "72.920860"
        let myUrl = "http://maps.apple.com/?ll=\(locationLat),\(locationlong)"
        
        if let url = URL(string: "\(myUrl)") {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
}

