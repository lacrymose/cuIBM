/**
 * \file generateA.h
 * \brief Declaration of the kernels to generate the matrix 
 *        resulting from the implicit terms in the momentum equation.
 */


#pragma once

#include "utilities/types.h"


/**
 * \namespace kernels
 * \brief Contains all the custom-written CUDA kernels.
 */
namespace kernels
{

// generate a block of the matrix resulting from implicit terms in the momentum equation
__global__
void generateA(int *ARows, int *ACols, real *AVals,
               real *MVals,
               int *LRows, int *LCols, real *LVals,
               int ASize, real alpha);

// generate a block of the matrix resulting from implicit terms in the momentum equation
// for the direct forcing method
__global__
void generateADirectForcing(int *ARows, int *ACols, real *AVals,
                            real *MVals,
                            int *LRows, int *LCols, real *LVals,
                            int ASize, real alpha, int *tags);

} // End of namespace kernels
