
namespace CrackingTheCodingInterview
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnStringCompression = new System.Windows.Forms.Button();
            this.txtInput = new System.Windows.Forms.TextBox();
            this.txtOut = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btnStringCompression
            // 
            this.btnStringCompression.Location = new System.Drawing.Point(402, 12);
            this.btnStringCompression.Name = "btnStringCompression";
            this.btnStringCompression.Size = new System.Drawing.Size(81, 38);
            this.btnStringCompression.TabIndex = 0;
            this.btnStringCompression.Text = "String Compression";
            this.btnStringCompression.UseVisualStyleBackColor = true;
            this.btnStringCompression.Click += new System.EventHandler(this.btnStringCompression_Click);
            // 
            // txtInput
            // 
            this.txtInput.Location = new System.Drawing.Point(26, 22);
            this.txtInput.Name = "txtInput";
            this.txtInput.Size = new System.Drawing.Size(178, 20);
            this.txtInput.TabIndex = 1;
            this.txtInput.Text = "aabcccccaaa";
            // 
            // txtOut
            // 
            this.txtOut.Location = new System.Drawing.Point(227, 22);
            this.txtOut.Name = "txtOut";
            this.txtOut.Size = new System.Drawing.Size(153, 20);
            this.txtOut.TabIndex = 2;
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(495, 73);
            this.Controls.Add(this.txtOut);
            this.Controls.Add(this.txtInput);
            this.Controls.Add(this.btnStringCompression);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "frmMain";
            this.Text = "Cracking The Coding Interview";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnStringCompression;
        private System.Windows.Forms.TextBox txtInput;
        private System.Windows.Forms.TextBox txtOut;
    }
}

