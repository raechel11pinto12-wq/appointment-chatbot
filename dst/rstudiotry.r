# Sample continuous dataset
set.seed(42)
data_vec <- c(rnorm(200, mean = 25, sd = 5), rnorm(100, mean = 32, sd = 3))

# Calculate Median and Mode
median_val <- median(data_vec)
dens <- density(data_vec)
mode_val <- dens$x[which.max(dens$y)]

# Draw Histogram
hist(data_vec, 
     col = "skyblue", 
     border = "white",
     main = "Histogram with Mode and Median",
     xlab = "Values")

# Add Vertical Lines for Median and Mode
abline(v = median_val, col = "red", lwd = 2, lty = 2)     # Red dashed line for Median
abline(v = mode_val, col = "darkgreen", lwd = 2, lty = 1) # Green solid line for Mode

# Add Legend
legend("topright", 
       legend = c(paste("Median:", round(median_val, 2)), 
                  paste("Mode:", round(mode_val, 2))),
       col = c("red", "darkgreen"), 
       lty = c(2, 1), 
       lwd = 2)